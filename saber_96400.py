import glob

def main() -> None:
    # ---------- Start of variable part ------------------
    
    # TODO change only this vars

    INPUT_PATH_MASK = "./input/*.nc"
    OUTPUT_PATH = "./output"

    # ----------- End of variable part -------------------

    print("Script is started")

    files = glob.glob(INPUT_PATH_MASK)
    for filepath in files:
        print(f"Process >> {filepath}")

        try:
            print("    Step 1 - ") 

            print("    Step 2- ") 

            print("    Step 3 - ") 

            print("    Step 4 - ") 

        except Exception as e:
            print(f"    Cannot process >> {filepath}")
            print(f"    Error >> {str(e)}")
        finally:
            print()

    print("Script is ended")

if __name__ == '__main__':
    main()