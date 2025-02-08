import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
import numpy as np

# Dummy dataset generation
def generate_dummy_data(num_samples=1000, input_size=10):
    X = np.random.rand(num_samples, input_size)
    y = (X.sum(axis=1) > (input_size / 2)).astype(float)  # Binary classification
    return X, y

# Define a simple MLP model
class SimpleMLP(nn.Module):
    def __init__(self, input_size, hidden_size=16):
        super(SimpleMLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x

# Train function
def train_model(model, X_train, y_train, X_val, y_val, epochs=100, lr=0.01):
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
    X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
    y_val_tensor = torch.tensor(y_val, dtype=torch.float32).view(-1, 1)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = criterion(outputs, y_train_tensor)
        loss.backward()
        optimizer.step()
        
        if epoch % 10 == 0:
            model.eval()
            val_outputs = model(X_val_tensor)
            val_loss = criterion(val_outputs, y_val_tensor)
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}, Val Loss: {val_loss.item():.4f}")

# Function to test the trained model on new data
def test_model(model, X_test):
    model.eval()
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    predictions = model(X_test_tensor).detach().numpy()
    return predictions

if __name__ == "__main__":
    input_size = 10
    X, y = generate_dummy_data(num_samples=1000, input_size=input_size)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = SimpleMLP(input_size)
    train_model(model, X_train, y_train, X_val, y_val)
    
    # Generate new dummy test data
    X_test, _ = generate_dummy_data(num_samples=5, input_size=input_size)
    predictions = test_model(model, X_test)
    print("Predictions on new data:", predictions)
