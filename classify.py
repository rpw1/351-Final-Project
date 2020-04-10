from mnist import MNIST

mndata = MNIST('./mnistData')

training_images, training_labels = mndata.load_training()

test_images, test_labels = mndata.load_testing()

image = test_images[0]

# print(mndata.display(training_images[0]))

# print(mndata.display(test_images[0]))