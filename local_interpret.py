def local_interpret(prs: float) -> str:
    """
    Interpret the PRS score.
    Returns a formatted string containing the risk assessment.
    """
    
    output = []
    output.append("\n\n" + "="*60)
    output.append("Alzheimer's Disease Risk Assesment") 
    output.append("="*60 + "\n")
    
    output.append("Your polygenic risk score (PRS) is:  " + str(prs))
    output.append("")
    
    if prs > 1.2:
        output.append("\033[91mHIGH RISK\033[0m")  # Red
    elif prs > 0.8:
        output.append("\033[0mMODERATE RISK\033[0m")  # Normal
    else:
        output.append("\033[92mLOW RISK\033[0m")  # Green
        
    output.append("\n" + "="*60 + "\n")
    
    return "\n".join(output)