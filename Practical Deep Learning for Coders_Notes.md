# Practical Deep Learning for Coders - Full Course from fast.ai and Jeremy Howard


<https://www.youtube.com/watch?v=0oyCUWLL_fU>


## Machine learing
![](Practical%20Deep%20Learning%20for%20Coders_IMG/machine%20learning%20concept%20map.png)
If we could enumerate all the possible ways of playing checkers, and then describe each of those ways using some set of parameters or what Arthur Samuel called weights. Then if we had a way of checking how effective a current weight assignment  is in terms of actual performance. In other words, does that particular enumeration of a strategy for playing checkers end up wining or losing games? The way to alter the weight assignment so as to maximize the performance. So let's try increasing or decreasing each one of those weights one at a time to find out if there is a slightly better way of playing checkers. Do this action lots of times. Eventually such a procedure could be made entirely automatic. And then the machine so programmed would learn from its experience. This is machine learning. This is machine learning, a way of creating programs such that they can learn rather than they are programmed. 机器学习是一种通过根据最终表现，优化权重分配，不对解决问题进行具体编程，而解决问题的方式。 Therefore a trained model can be used just like any other computer program. So the idea is we build a computer program, not by putting out the steps necessary to do the task, but by training it to learn to do the task. At the end of which it is just another program. This is what is called inference.

![](Practical%20Deep%20Learning%20for%20Coders_IMG/image2.png)
The training of programs developed by allowing a computer to learn from its experience, rather than through manually coding the individual steps.

## Neural Networks

It is not at all obvious what the method might look like for an image recognition program, or for understanding text, or for many other interesting problems we might imagine.
What we would like is some kind of function that is so flexible that it could be used to solve any given problem, just by varying its weights. Amazingly enough, this function actually exists! It is the neural network.神经网络是一种解决问题的通用函数，只需要通过变化权重。
A mathematical proof called the universal approximation theorem shows that this function can solve any problem to any level of accuracy, in theory.
![](Practical%20Deep%20Learning%20for%20Coders_IMG/image2.png)

在训练过程中，根据表现不断调整，找到好的权重分配是工作目的。这也被叫做Stochastic Gradient Descent（SGD）
![](Practical%20Deep%20Learning%20for%20Coders_IMG/image3.png)