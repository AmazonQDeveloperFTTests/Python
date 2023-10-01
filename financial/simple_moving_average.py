"""
Calculate the Simple Moving Average (SMA) for a time series data.
https://en.wikipedia.org/wiki/Moving_average
"""


def simple_moving_average(data: list[float], window_size: int) -> list[float]:
    """


    :param data: A list of numerical data points.
    :param window_size: An integer representing the size of the SMA window.
    :return: A list of SMA values with the same length as the input data.

    The Simple Moving Average (SMA) is a statistical calculation used to
    analyze data points by creating
    a constantly updated average price over a specific time period.
    In finance, SMA is often used in technical
    analysis to smooth out price data and identify trends.

    Example:
    >>> sma = simple_moving_average([10, 12, 15, 13, 14, 16, 18, 17, 19, 21], 3)
    >>> [round(value, 2) if value is not None else None for value in sma]
    [None, None, 12.33, 13.33, 14.0, 14.33, 16.0, 17.0, 18.0, 19.0]
    """

    sma = []
    for i in range(len(data)):
        if i < window_size - 1:
            sma.append(None)  # SMA not available for early data points
        else:
            window = data[i - window_size + 1 : i + 1]
            sma_value = sum(window) / window_size
            sma.append(sma_value)
    return sma


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example data (replace with your own time series data)
    data = [10, 12, 15, 13, 14, 16, 18, 17, 19, 21]

    # Specify the window size for the SMA
    window_size = 3

    # Calculate the Simple Moving Average
    sma_values = simple_moving_average(data, window_size)

    # Print the SMA values
    print("Simple Moving Average (SMA) Values:")
    for i, value in enumerate(sma_values):
        if value is not None:
            print(f"Day {i + 1}: {value:.2f}")
        else:
            print(f"Day {i + 1}: Not enough data for SMA")
