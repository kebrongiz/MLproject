import tensorflow as tf
name = tf.Variable("kebron", tf.string)
age = tf.Variable(23, tf.int32)
test = tf.Variable(["Test"], tf.string)
rank_tensor1 = tf.Variable(["Test", "Name", "Gread"], tf.string)
rank_tensor2 = tf.Variable(["Id no", "class", "ok"], ["Name", "ok", "ok"], tf.string)

#rank of tensor
print(tf.rank(rank_tensor1))
#shape of tensor
print(test.shape)
print(rank_tensor1.shape)
print(rank_tensor2.shape)
print(tf.shape(rank_tensor2))
