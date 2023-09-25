cross_entropy = np.sqrt(tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
cross_entropy = tf.sqrt(tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1])))
