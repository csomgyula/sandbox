def feature(lines):
    """
    Feature function to score lines based on whether they are preceded or followed by an empty line.
    Headings are more likely to be surrounded by empty lines.
    
    Args:
        lines (list of str): The lines of the text.
    
    Returns:
        list of float: Scores between 0 and 1 indicating heading likelihood.
    
    Examples:
        >>> feature(["Heading", "", "Paragraph text.", "Paragraph text.", "Another Heading", "", "More text."])
        [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
    """
    liness = [line.strip() for line in lines]
    scores = [0.0] * len(liness)
    
    for i, line in enumerate(liness):
        if not (line == ""):  # Non-empty line
            next_empty = (i < len(liness) - 1 and  (liness[i + 1] == ""))
            if next_empty:
               scores[i] = 1.0
    return scores

if __name__ == "__main__":
    import doctest
    doctest.testmod()
