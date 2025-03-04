def fun(data, batch_size):
    data_size = len(data)
    for start_index in range(0, data_size, batch_size):
        end_index = min(start_index + batch_size, data_size)
        batch_data = data[start_index:end_index]  # Use a different variable name
        print(f"Processing data from {start_index} to {end_index}")
        print(batch_data)

data = list(range(400))
fun(data, 100)
