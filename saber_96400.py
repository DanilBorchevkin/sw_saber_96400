import glob
import xarray as xr
from pathlib import Path
import time


class RunTimer:
    def __init__(self) -> None:
        self.start_time = time.time()

    def stop(self) -> str:
        self.stop_time = time.time()

        self.execution_time = self.stop_time - self.start_time

        return f"{self.execution_time : .2f}"


def formatter_date(arr) -> str:
    return f"{arr.data : .0f}".lstrip()


def formatter_float32(arr) -> str:
    ret_str = f"{arr.data : g}".lstrip()

    if ret_str == 'nan':
        return 'None'
    else:
        return ret_str


def nc_file_extract_data(filepath: str, is_verbose: bool = False) -> list:
    out_data = list()

    # Open data set
    dataset = xr.open_dataset(filepath)
    
    # Print information about dataset if needed
    if (is_verbose):
        print()
        print("[NC-->DAT] Dataset information >>")
        print(dataset)
        print()

    # Get event coordinates
    coord_event = dataset.coords['event'].data

    # Get altitude coordinates
    coord_alt = dataset.coords['altitude'].data

    for event in coord_event:
        if (is_verbose):
            print(f"[NC-->DAT] Process event >> {event}")

        # Create sub dataset only for event coordinate
        dataset_sub_event = dataset.sel(event=event)

        # Create basic data and append constant variables for the each event which dont depend on altitude here
        record_base_data = list()
        record_base_data.append(event)
        record_base_data.append(formatter_date(dataset_sub_event.data_vars['date']))

        for idx, alt in enumerate(coord_alt):
            if (is_verbose):
                print(f"[NC-->DAT] Process alt >> {alt}")

            # Create new empty record
            record = list()

            # Extend it by base data
            record.extend(record_base_data)

            # Create sub sub dataset for event + alt
            dataset_sub_event_alt = dataset_sub_event.sel(altitude=alt)
            data_vars = dataset_sub_event_alt.data_vars

            # Append variables depend on altitude
            record.append(formatter_float32(data_vars['CO2']))
            record.append(formatter_float32(data_vars['density']))
            record.append(formatter_float32(data_vars['elevation']))
            record.append(formatter_float32(data_vars['H']))
            record.append(formatter_float32(data_vars['H2O']))
            record.append(formatter_float32(data_vars['ktemp']))
            record.append(formatter_float32(data_vars['NO_ver']))
            record.append(formatter_float32(data_vars['NO_ver_top']))
            record.append(formatter_float32(data_vars['NO_ver_top_unfilt']))
            record.append(formatter_float32(data_vars['O']))
            record.append(formatter_float32(data_vars['O2_1delta_ver']))
            record.append(formatter_float32(data_vars['O2_1delta_ver_unfilt']))
            record.append(formatter_float32(data_vars['O3_127']))
            record.append(formatter_float32(data_vars['O3_96']))
            record.append(formatter_float32(data_vars['OH_16_ver']))
            record.append(formatter_float32(data_vars['OH_16_ver_unfilt']))
            record.append(formatter_float32(data_vars['OH_20_ver']))
            record.append(formatter_float32(data_vars['pressure']))
            record.append(formatter_float32(data_vars['time']))
            record.append(formatter_float32(data_vars['time_top']))
            record.append(formatter_float32(data_vars['tpaltitude']))
            record.append(formatter_float32(data_vars['tpaltitude_top']))
            record.append(formatter_float32(data_vars['tpgpaltitude']))
            record.append(formatter_float32(data_vars['tplatitude']))
            record.append(formatter_float32(data_vars['tplatitude_top']))
            record.append(formatter_float32(data_vars['tplongitude']))
            record.append(formatter_float32(data_vars['tplongitude_top']))

            out_data.append(record)

    return out_data


def data_process(data: list):
    out_data = list()

    out_data = data

    return out_data


def dat_file_data_save(filepath: str, data: list, header: list = None) -> None:
    write_list = list()

    for record in data:
        output_str = ""

        for val in record:
            output_str += str(val) + "\t"

        output_str = output_str[:-1]
        output_str += "\n"

        write_list.append(output_str)

    with open(filepath, "w") as f:
        f.writelines(write_list)

    return None


def main() -> None:
    # ---------- Start of variable part ------------------
    # TODO change only this vars

    INPUT_PATH_MASK = "./input/*.nc"
    OUTPUT_PATH = "./output"

    # ----------- End of variable part -------------------

    print("[NC-->DAT] Script is started")

    run_timer = RunTimer()

    files = glob.glob(INPUT_PATH_MASK)
    for filepath in files:
        print(f"[NC-->DAT] Process >> {filepath}")

        try:
            print("    Step 1 - Extract data")
            data = nc_file_extract_data(filepath)

            print("    Step 2 - Process data")
            processed_data = data_process(data)

            print("    Step 3 - Save data")
            out_filepath = f"{OUTPUT_PATH}/{Path(filepath).stem}_out.dat"
            dat_file_data_save(out_filepath, processed_data)
            print(f"        Saved to {out_filepath}")

        except Exception as e:
            print(f"    Cannot process >> {filepath}")
            print(f"    Error >> {str(e)}")

        finally:
            pass

    if len(files) == 0:
        print(f"[NC-->DAT] No files found at >> {INPUT_PATH_MASK}")

    print(f"[NC-->DAT] Script is ended. Run time is {run_timer.stop()} seconds")


if __name__ == '__main__':
    main()
