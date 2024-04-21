"""
Demonstration of how to return an image generated with numpy and a plot
generated with matplotlib using the Flask web server.

Requirements: numpy, flask, scikit-image, matplotlib.
"""

# import cStringIO as StringIO
from io import StringIO, BytesIO
from flask import Flask, send_file
import numpy as np
from skimage.io import imsave
import matplotlib.pyplot as plt

app = Flask(__name__)
app.debug = True


@app.route('/')
def generate_image():
    """
    Return a generated image as a png by
    saving it into a StringIO and using send_file.
    """
    num_tiles = 20
    tile_size = 30
    arr = np.random.randint(0, 255, (num_tiles, num_tiles, 3))
    arr = arr.repeat(tile_size, axis=0).repeat(tile_size, axis=1)

    # We make sure to use the PIL plugin here because not all skimage.io plugins
    # support writing to a file object.
    strIO = BytesIO()
    imsave(strIO, arr, plugin='pil', format_str='png')
    strIO.seek(0)
    return send_file(strIO, mimetype='image/png')


@app.route('/plot')
def generate_plot():
    """
    Return a matplotlib plot as a png by
    saving it into a StringIO and using send_file.
    """
    def using_matplotlib():
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.path import Path
        import matplotlib.patches as patches
        n = 8  # Number of possibly sharp edges
        r = .7  # magnitude of the perturbation from the unit circle,
        # should be between 0 and 1
        N = n * 3 + 1  # number of points in the Path
        # There is the initial point and 3 points per cubic bezier curve. Thus, the curve will only pass though n points, which will be the sharp edges, the other 2 modify the shape of the bezier curve

        angles = np.linspace(0, 2 * np.pi, N)
        codes = np.full(N, Path.CURVE4)
        codes[0] = Path.MOVETO


        verts = np.stack((np.cos(angles), np.sin(angles))).T * (2 * r * np.random.random(N) + 1 - r)[:, None]
        verts[-1, :] = verts[0, :]  # Using this instad of Path.CLOSEPOLY avoids an innecessary straight line
        path = Path(verts, codes)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        patch = patches.PathPatch(path, facecolor='none', lw=2)
        ax.add_patch(patch)

        ax.set_xlim(np.min(verts) * 1.1, np.max(verts) * 1.1)
        ax.set_ylim(np.min(verts) * 1.1, np.max(verts) * 1.1)
        ax.axis('off')  # removes the axis to leave only the shape

        # plt.show()
        # fig = plt.figure(figsize=(6, 6), dpi=300)
        # ax = fig.add_subplot(111)
        # x = np.random.randn(900)
        # y = np.random.randn(900)
        # ax.plot(x, y, '.', color='r', markersize=10, alpha=0.2)
        # ax.set_title('Behold')

        strIO = BytesIO()
        plt.savefig(strIO, dpi=fig.dpi)
        strIO.seek(0)
        return strIO

    strIO = using_matplotlib()
    return send_file(strIO, mimetype='image/png')


# @app.route('/plot1')
# def generate_plot():
#     """
#     Return a matplotlib plot as a png by
#     saving it into a StringIO and using send_file.
#     """
#     def using_matplotlib():
#         fig = plt.figure(figsize=(6, 6), dpi=300)
#         ax = fig.add_subplot(111)
#         x = np.random.randn(900)
#         y = np.random.randn(900)
#         ax.plot(x, y, '.', color='r', markersize=10, alpha=0.2)
#         ax.set_title('Behold')
#
#         strIO = BytesIO()
#         plt.savefig(strIO, dpi=fig.dpi)
#         strIO.seek(0)
#         return strIO
#
#     strIO = using_matplotlib()
#     return send_file(strIO, mimetype='image/png')


if __name__ == '__main__':
    app.run()
