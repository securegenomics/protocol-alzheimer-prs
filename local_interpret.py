def local_interpret(prs: float) -> str:
    """
    Interpret the PRS score.
    Returns a formatted string containing the risk assessment.
    """
    # Define colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    END = "\033[0m"
    
    output = []
    
    output.append(BLUE + "\n\n" + "="*60)
    output.append("Alzheimer's Disease Risk Assesment") 
    output.append("="*60 + END + "\n")
    
    output.append("Your polygenic risk score (PRS) is:  " + "{:.2f}".format(prs))
    output.append("")
    
    if prs > 1.2:
        output.append(RED + "HIGH RISK" + END)
    elif prs > 0.8:
        output.append(BLUE + "MODERATE RISK" + END)
    else:
        output.append(GREEN + "LOW RISK" + END)
        
    output.append(BLUE + "\n" + "="*60 + END + "\n")
    
    return "\n".join(output)