def feature(lines):
    """
    Feature function to score lines based on their length.
    Shorter lines are more likely to be headings.
    
    Args:
        lines (list of str): The lines of the text.
    
    Returns:
        list of float: Scores between 0 and 1 indicating heading likelihood.
    
    Examples:
        >>> feature(["Introduction", "This is a longer sentence.", "Conclusion"])
        [1.0, 0.0, 1.0]
        
        >>> feature(["Short", "A much longer text line that is likely not a heading.", "Another short one"])
        [1.0, 0.0, 1.0]
    """
    import numpy as np
    
    lengths = np.array([len(line.strip()) for line in lines])
    
    if len(lengths) == 0:
        return []
    
    threshold = np.percentile(lengths, 25)  # Lower quartile as dynamic threshold
    max_length = np.max(lengths) if np.max(lengths) > 0 else 1  # Avoid division by zero
    
    scores = np.clip(1 - (lengths / max_length), 0, 1)  # Normalize and invert score
    scores[lengths <= threshold] = 1  # Strong heading candidate if very short
    
    return scores.tolist()
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()