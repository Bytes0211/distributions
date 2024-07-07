# make_blobs genrates isotropic Gaussian blobs for clustering
from resources import datum
import numpy as np
from bokeh.models import ColumnDataSource, curdoc, figure, output_file, save 
import bokeh.colors.named as colors
from bokeh.layouts import row 
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import sympy as sp 
from IPython.display import display, Markdown
import sys 
sys.path.insert(0, '..')


class InvalidParamEntry(Exception):
    """Raised when invalid parameter is passed"""


class InvalidParamValue(Exception):
    """Raised when invalid parameter is passed"""


class InvalidClassAction(Exception):
    """Raised when invalid parameter is passed"""


class Model:
    def __init__(self, 
                 X: np.ndarray = np.empty([0, 0]),
                 y: np.ndarray = np.empty([0, 0]),
                 n_samples=1000,
                 n_features=2, 
                 centers=2,
                 random_state=42
                 ):

        self.calc = datum.Data()
        self.X = X
        self.y = y
        self.n_samples = n_samples
        self.n_features = n_features
        self.centers = centers
        self.random_state = random_state
        self.created = False
        
    def get_blobs(self,
                  file: str, 
                  centers: int = 2,
                  samples: int = 1000,
                  features: int = 2,
                  rdm: int = 1,
                  cluster_std: float = 1,
                  std_norm: bool = False) -> tuple:
        """
        Generate synthetic blobs dataset for binary classification.

        Parameters:
        - centers (int): The number of centers to generate.
        - samples (int): The total number of points divided among clusters.
        - features (int): The number of features for each sample.
        - rdm (int): andom seed for dataset generation.
        - cluster_std (float): The standard deviation of the clusters.
        - std_norm (bool): Flag indicating whether to standardize the features. 
 
        Returns: 
        - X (ndarray): The generated feature matrix. 
        - y (ndarray): The generated target vector. 
 
        """ 
        X, y = make_blobs(n_samples=samples, 
                          centers=centers, 
                          n_features=features, 
                          random_state=rdm, 
                          cluster_std=cluster_std) 
         
        # Standardize features if required 
        if std_norm: 
            calc = datum.Data() 
            X[:, 0] = calc.convert_to_std_norm(X[:, 0]) 
            X[:, 1] = calc.convert_to_std_norm(X[:, 1]) 
            X_mu = "{:f}".format(np.mean(X[:, 0])) 
            X_sigma = np.std(X[:, 0]) 
        else:
            X_mu = f'{np.mean(X[:, 0]): .2f}'
            X_sigma = f'{np.std(X[:, 0]): .2f}'
            
        data = '<br><br>\r$\\displaystyle \\text{X shape: (%s, %s)}\\qquad \
        X_{min}: %s\\qquad X_{max}: %s$<br>\r'

        data = data + '<br><br>\r$\\displaystyle \\text{y shape: %s}$<br>\r'
        data = data + '<br><br>\r$\\displaystyle \\mu_x = %s,~ \\sigma_x \
        = %s$<br>\r'

        data = data + '<br><br>\r$\\displaystyle \\sigma_y = %s$<br>\r'
        data = data + '<br><br>\r$\\displaystyle \\text{First 5 rows of X:}$ \
        <br>\r$%s$<br><br>\r'

        data = data + '<br><br>\r$\\displaystyle \\text{First 5 rows of y:}$ \
        <br>\r$%s$<br><br>\r'

        display(Markdown(data % (
            X.shape[0], X.shape[1],
            f'{np.min(X[:, 0]): .2f}', f'{np.max(X[:, 0]): .2f}', 
            y.shape[0],
            X_mu, X_sigma, 
            f'{np.std(y): .2f}',
            sp.latex(sp.Matrix(X[:5].round(2))),
            sp.latex(sp.Matrix(y[:5]))
            )))
        
        label_colors = [
                colors.olivedrab if i == 0
                else colors.slateblue
                for i in y
                ]

        data_dict = dict(x=X[:, 0], y=X[:, 1], label_color=label_colors)
        source = ColumnDataSource(data=data_dict)

        curdoc().theme = 'dark_minimal'

        plot = figure(title=f'Simple Binary Classification with cluster \
                standardard deviation set to {cluster_std}\n',
                      x_axis_label='X_0',
                      y_axis_label='X_1', 
                      width=800,
                      height=600
                      )

        plot.scatter(marker='circle',
                     x='x',
                     y='y',
                     size=10,
                     source=source,
                     color='label_color')
        output_file('../docs/bokeh/' + file)
        save(plot)
        self.created = True
        self.X = X
        self.y = y
        return X, y

    def get_train_test_split(self,
                             test_size: float = 0.2,
                             rdm: int = 42,
                             show_plot=False) -> tuple:
        """
        Split the data into training and testing sets.

        Parameters:
        - test_size (float): The proportion of the dataset to include in \
                the test split.
        - rdm (int): The random seed for reproducibility.

        Returns:
        - tuple: A tuple containing the training and testing sets.

        Raises:
        - InvalidClassAction: If the model has not been created and X, y values are not available.
        """
        if self.created:
            X_train, X_test, y_train, y_test = train_test_split(self.
                                                                X,self.y,
                                                                ,test_size=test_size
                                                                ,random_state=rdm)

            data = '<br><br>\r$\\displaystyle \\text{X-train shape: (%s, %s)} \
            \\qquad \\text{X-test shape: (%s, %s)}$<br>\r'

            data = data + '<br><br>\r$\\displaystyle \\text{y-train shape: %s} \
            \\qquad \\text{y-test shape: %s}$<br>\r'

            data = data + '<br><br>\r$\\displaystyle \\text{First 5 rows of \
            X-train:}$<br>\r$%s$<br><br>\r'

            data = data + '<br><br>\r$\\displaystyle \\text{First 5 rows of \
            y-train:}$<br>\r$%s$<br><br>\r'

            data = data + '<br><br>\r$\\displaystyle \\text{First 5 rows of \
            X-test:}$<br>\r$%s$<br><br>\r'

            data = data + '<br><br>\r$\\displaystyle \\text{First 5 rows of \
             y-test:}$<br>\r$%s$<br><br>\r'

            display(Markdown(data % (
                X_train.shape[0],
                X_train.shape[1],
                X_test.shape[0],
                X_test.shape[1],
                y_train.shape[0],
                y_test.shape[0],
                sp.latex(sp.Matrix(X_train[:5].round(2))),
                sp.latex(sp.Matrix(y_train[:5])),
                sp.latex(sp.Matrix(X_test[:5].round(2))),
                sp.latex(sp.Matrix(y_test[:5]))
            )))
            
            if show_plot:
                curdoc().theme = 'dark_minimal'
                # train plot 
                train_label_colors = [
                        colors.olivedrab if i == 0
                        else colors.slateblue
                        for i in y_train
                        ]
                train_data_dict = dict(x=X_train[:, 0],
                                       y=X_train[:, 1],
                                       label_color=train_label_colors)
                train_source = ColumnDataSource(data=train_data_dict)
                
                train_plot = figure(title=f'Train Data - {len(X_train[:, 0])} \
                        Observations\n',
                                    x_axis_label='X-Train-0',
                                    y_axis_label='X-Train-1',
                                    width=550,
                                    height=450)
                
                train_plot.scatter(marker='circle',
                                   x='x',
                                   y='y',
                                   size=10,
                                   source=train_source,
                                   color='label_color')
                
                # test plot 
                test_label_colors = [
                        colors.olivedrab if i == 0 else colors.slateblue
                        for i in y_test]
                test_data_dict = dict(x=X_test[:, 0],
                                      y=X_test[:, 1],
                                      label_color=test_label_colors)
                test_source = ColumnDataSource(data=test_data_dict)
                                
                test_plot = figure(title=f'Test Data - {len(X_test[:, 0])} \
                        Observations\n',
                                   x_axis_label='X-Test-0',
                                   y_axis_label='X-Test-1',
                                   width=550,
                                   height=450)

                test_plot.scatter(marker='circle',
                                  x='x',
                                  y='y',
                                  size=10,
                                  source=test_source,
                                  color='label_color')
                
                save(row(train_plot, test_plot))
            return X_train, X_test, y_train, y_test
        else:
            err_msg = 'Model Not Created. X and y values are not available'
            raise InvalidClassAction(err_msg)
