from pycaret.datasets import get_data
insurance = get_data('insurance')

# Initialize environment
from pycaret.regression import *
r1 = setup(insurance, target = 'charges', session_id = 123,
           normalize = True,
           polynomial_features = True, trigonometry_features = True,
           feature_interaction=True, 
           bin_numeric_features= ['age', 'bmi'])

# Train a linear regression model
lr = create_model('lr')
