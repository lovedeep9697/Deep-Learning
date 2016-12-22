import numpy as np


class NeuralNet:

	def __init__(self,architect):
		'''architect defines the architecture of the Neural Network'''

		'''number of elements in architect gives the number of layers
		the first and last element denote the input and output layer

		The value of each element gives the number of neurons in that 
		layer

		number of neurons in input = number of features
		number of neurons in output layer = number of output features
											(this may be greater than 1 such as in case of MNIST
											 there output features represent the probabilities
											 of an image belonging to a particular class)
		'''

		self.architect = architect
		self.num_layer = len(architect)
		self.weights = [np.random.randn(early,new) for early,new in zip(size[:-1],size[1:])]
		self.biases  = [np.random.randn(neurons) for neurons in size[1:]]


	def activation(tensor,activ = 'relu'):

		if activ == 'relu':
			return tensor*(tensor>0)

		if activ == 'tanh':
			return np.tanh(tensor)

		if activ == 'sigmoid':
			return 1.0/(1.0 + np.exp(-tensor))


	def sigmoid_prime(tensor):

		tmp = activation(tensor,activ = 'sigmoid')
		return tmp*(1-tmp)


	def feedforward(self,x,y):

		'''performs forwardprop on a single batch'''
		
		prediction = x			
		for weights,biases in zip(self.weights,self.biases):
			prediction = np.dot(prediction,weights)
			for row in prediction:
				row += biases

			prediction = activation(prediction)

		# now prediction is num_samples X num_output_features
		return prediction


	def backprop(self):
		pass

	def cost(self):
		pass


	def train(self,x_train,y_train,eta = 0.001,batch_size = 1,epochs = 100):
		'''Makes batches, applies feedforward and backprop'''
		'''ASSUMPTIONS:- 
		x_train : num_samples X num_features
		y_train : num_samples X num_output_features

		OUTPUT:- 
		training_log : cost vs epoch
		'''

		num_samples = len(y_train)
		num_features = self.architect[0]
		num_output_features = self.architect[-1] 

		# making batches
		batch_data = []
		X = 0
		TARGET = 1

		if batch_size == 1:
			batch_data = [ ( x.reshape((1,num_features)) , y.reshape((1,num_output_features)) ) for x,y in zip(x_train,y_train) ]
		
		else:
			batch_data = [ (x_train[k:k+batch_size],y_train[k:k+batch_size])

			               for k in range(0,num_samples,batch_size) ]

		# training starts
		training_log = []
		for epoch in range(epochs):

			for x,y in batch_data:
				
				# FEEDFORWARD
				activations = self.feedforward(x,y)	# now prediction is batch_size X num_output_features

				# BACKPROP
				delta_w, delta_b = self.backprop(y,prediction)  # delta_w and delta_b structurally 
													   # similar to weights and biases

				# UPDATION
				alpha = eta/num_samples
				self.weights = [ weights + alpha * dw for weights,dw in zip(self.weights,delta_w)  ]
				self.biases = [ biases + alpha * db for biases,db in zip(self.biases,delta_b) ]

			total_prediction
			training_log.append(self.cost(x_train,y_train))