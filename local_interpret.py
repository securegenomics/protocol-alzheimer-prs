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
    
    def red(text):
        return RED + text + END
    def green(text):
        return GREEN + text + END
    def blue(text):
        return BLUE + text + END
    
    risk_level = (
        red("HIGH RISK") if prs > 1.2
        else blue("MODERATE RISK") if prs > 0.8
        else green("LOW RISK")
    )
    
    return f'''{blue("\n\n" + "="*60)}
{blue("Alzheimer's Disease Risk Assesment")}
{blue("="*60 + "\n")}
{blue(f"Your polygenic risk score (PRS) is:  {prs:.2f}")}

{risk_level}
{blue("\n" + "="*60 + "\n")}'''