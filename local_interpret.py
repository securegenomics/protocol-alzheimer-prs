
def local_interpret(prs: float) -> str:
    """
    Interpret the PRS score.
    """
    
    print("\n\n" + "="*60)
    print("Alzheimer's Disease Risk Assesment")
    print("="*60 + "\n")
    
    print("Your polygenic risk score (PRS) is:" + str(prs))
    print()
    
    
    if prs > 1.2:
        print("\033[91mHIGH RISK\033[0m")  # Red
    elif prs > 0.8:
        print("\033[0mMODERATE RISK\033[0m")  # Normal
    else:
        print("\033[92mLOW RISK\033[0m")  # Green
        
    print("\n" + "="*60 + "\n")
        
        
        
        
        