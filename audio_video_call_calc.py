import pandas as pd

# Loading the dataset
file_path = r"C:\Users\jluba\mi3\audio_video_calculation\Data Engineer - ipdr.xlsx"
df = pd.read_excel(file_path)

# Fixing the datetime format issue by adding a space before parsing
df["starttime"] = df["starttime"].astype(str).str.replace(r"(\d{4}-\d{2}-\d{2})(\d{2}:\d{2}:\d{2})", r"\1 \2", regex=True)
df["endtime"] = df["endtime"].astype(str).str.replace(r"(\d{4}-\d{2}-\d{2})(\d{2}:\d{2}:\d{2})", r"\1 \2", regex=True)

# Converting timestamps
df["starttime"] = pd.to_datetime(df["starttime"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
df["endtime"] = pd.to_datetime(df["endtime"], format="%Y-%m-%d %H:%M:%S", errors="coerce")

# Converting volumes from Bytes to KB
df["dlvolume_kb"] = df["dlvolume"] / 1024
df["ulvolume_kb"] = df["ulvolume"] / 1024

# Grouping by MSISDN and Domain (VoIP App)
calls = []
for (msisdn, domain), group in df.groupby(["msisdn", "domain"]):
    group = group.sort_values("starttime").reset_index(drop=True)
    call_start = group.iloc[0]["starttime"]
    call_end = group.iloc[0]["endtime"]
    total_volume = 0
    fdr_count = 0

    for i in range(len(group)):
        row = group.iloc[i]
        if i == 0 or (row["starttime"] - call_end).total_seconds() > 600:
            # New Call
            if i > 0:
                duration = (call_end - call_start).total_seconds()
                bitrate = (total_volume * 8) / duration if duration > 0 else 0
                is_audio = bitrate <= 200
                is_video = bitrate > 200
                if bitrate >= 10:
                    calls.append([msisdn, domain, duration, fdr_count, bitrate, is_audio, is_video])

            # Reset for new call
            call_start = row["starttime"]
            total_volume = 0
            fdr_count = 0

        call_end = max(call_end, row["endtime"])
        total_volume += row["dlvolume_kb"] + row["ulvolume_kb"]
        fdr_count += 1

    # Save the last call
    duration = (call_end - call_start).total_seconds()
    bitrate = (total_volume * 8) / duration if duration > 0 else 0
    is_audio = bitrate <= 200
    is_video = bitrate > 200
    if bitrate >= 10:
        calls.append([msisdn, domain, duration, fdr_count, bitrate, is_audio, is_video])

# Converting results to DataFrame
output_df = pd.DataFrame(calls, columns=["msisdn", "domain", "duration_sec", "fdr_count", "kbps", "is_audio", "is_video"])

# Saving to CSV
output_path = r"C:\Users\jluba\mi3\audio_video_calculation\voip_calls_output.csv"
output_df.to_csv(output_path, index=False)
print(f"Output saved to: {output_path}")
