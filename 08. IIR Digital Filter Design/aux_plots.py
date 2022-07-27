import numpy as np
import matplotlib.pyplot as plt


def plot_zeros_poles(z, p):
    """
    Function that plots zeros and poles of transfer function

    Parameters:
    z (numpy array): Array of zeros.
    p (numpy array): Array of poles.

    Returns:
    Plot of zeros and poles of transfer function.

    """
    ax = plt.subplot(133)
    x = np.arange(-1, 1, 0.00001)
    y = np.zeros(len(x))
    ax.plot(x, np.sqrt(1 - x ** 2), 'black')
    ax.plot(x, -np.sqrt(1 - x ** 2), 'black')
    ax.plot(np.real(z), np.imag(z), 'bo', fillstyle='none', markersize=12)
    ax.plot(np.real(p), np.imag(p), 'rx', markersize=12)
    ax.grid(b=True, which='major')
    axis_x = np.arange(-1.5, 1.5, 0.00001)
    axis_y = np.zeros(len(axis_x))
    ax.plot(axis_x, axis_y, 'gray')
    ax.plot(axis_y, axis_x, 'gray')
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    plt.xlabel('Re')
    plt.ylabel('Im')
    return


def plot_frequency_response(x, f, title="Frequency Response of Filter", label=None):
        """
        Function to plot power frequency response of a given filter. Power of a signal x is calculated as
        follows P=20*log(x).
        :param x: (numpy array) input filter.
        :param f: (numpy array) normalized frequency between 0 and 0.5.
        :param title: (string) string of title to use.
        :param label: (string) string of label to use.
        :return: None
        """
        # We use this to avoid discontinuities in our plot
        x[0][0] = x[1][0]
        x[-1][0] = x[-2][0]

        x_log = 20 * np.log10(x)
        plt.plot(f, x_log, label=label)
        plt.title(title)
        plt.xlabel("Normalized frequency")
        plt.ylabel("Gain [dB]")
        plt.grid("on")
        return
