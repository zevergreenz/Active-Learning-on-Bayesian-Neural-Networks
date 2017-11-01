import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from basic_mnist import MnistModel


flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('data_dir', '../data', 'Data directory.')


def main(_):
  mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
  model = MnistModel()
  with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    model.optimize(mnist)
    acc = model.validate(mnist)
    print(acc)


if __name__ == '__main__':
  tf.app.run()








