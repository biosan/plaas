from io import BytesIO

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from .instruments import plot_lat

@plot_lat.time()  # Measure function execution time
def plot_it(title, data, streamable=False):
    """
    Return a simple XKCD-style line plot.
    Plot title and data are passed as arguments.

    Options:
      - If streamable == True, a ByteIO object is returned,
        else a bytearray object is returned.
    """
    # Build the plot
    plt.xkcd()
    plt.figure()
    plt.title = title
    plt.plot(data)

    # Save plot to image
    image = BytesIO()
    plt.savefig(image, format='png')
    plt.close()

    # Return plot image in the selected 'format'
    if streamable:
        return image
    else:
        return image.getvalue()