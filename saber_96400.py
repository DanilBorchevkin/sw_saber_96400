import glob


def nc_file_extract_data(filepath: str) -> list:
    out_data = list()

    # TODO do it

    return out_data


def data_process(data: list):
    out_data = list()

    # TODO do it

    return out_data


def dat_file_data_save(filepath: str, data: list) -> None:
    # TODO do it

    return None


def main() -> None:
    # ---------- Start of variable part ------------------
    # TODO change only this vars

    INPUT_PATH_MASK = "./input/*.nc"
    OUTPUT_PATH = "./output"

    # ----------- End of variable part -------------------

    print("[NC-->DAT] Script is started")

    files = glob.glob(INPUT_PATH_MASK)
    for filepath in files:
        print(f"[NC-->DAT] Process >> {filepath}")

        try:
            print("    Step 1 - Extract data")
            data = nc_file_extract_data(filepath)

            print("    Step 2 - Process data")
            processed_data = data_process(data)

            print("    Step 3 - Save data")
            out_filepath = f"{OUTPUT_PATH}/{filepath}_out.dat"
            dat_file_data_save(out_filepath, processed_data)
            print(f"        Saved to {out_filepath}")

        except Exception as e:
            print(f"    Cannot process >> {filepath}")
            print(f"    Error >> {str(e)}")

        finally:
            print()

    if len(files) == 0:
        print(f"[NC-->DAT] No files found at >> {INPUT_PATH_MASK}")

    print("[NC-->DAT] Script is ended")


if __name__ == '__main__':
    main()
