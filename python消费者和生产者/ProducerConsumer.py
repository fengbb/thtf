__author__ = 'DN'
#from threading import Thread,Lock
from threading import Condition,Thread
import time
import random
import queue
#queue = []
MAX_NUM = 10
#lock = Lock()
condition = Condition()
#我们开始了一个生产者线程（下称生产者）和一个消费者线程（下称消费者）。
#生产者不停地添加（数据）到队列，而消费者不停地消耗。
#由于队列是一个共享变量，我们把它放到lock程序块内，以防发生竞态条件。
#在某一时间点，消费者把所有东西消耗完毕而生产者还在挂起（sleep）。
# 消费者尝试继续进行消耗，但此时队列为空，出现IndexError异常。
#定义一个生产者类，继承Thread类
class ProducerThread(Thread):
    #定义一个run方法
    def run(self):
        #定义一个nums变量，存放一个能产生5个随机数的range变量
        nums = range(5)
        #will create the list [0,1,2,3,4]
        #print (nums)
        #range（0,5），range类型
        #for i in nums:
            #print (i)
            #0,1,2,3,4
        #定义一个全局变量queue
        global queue
        #定义一个死循环
        while True:
            #random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
            # 这里要说明一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
            #定义一个变量num，随机存放0,1,2,3,4中的一个数字
            num = random.choice(nums)
            #产生了死琐
            lock.acquire()
            #个全局queue追加一个数字
            queue.append(num)
            #打印生产的产品
            print ("Produced",num)
            #释放死锁
            lock.release()
            #随机暂停一段时间
            time.sleep(random.random())
#定义消费者类，继承Thread类
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            #产生死锁
            lock.acquire()
            #如果队为空
            if not queue:
                print ("Nothing in queue, but consumer will try to consume")
            #定义一个变量num，值为从queue中删除的值
            #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
            num = queue.pop(0)
            print ("Consumed",num)
            #释放死锁
            lock.release()
            time.sleep(random.random())
#ProducerThread().start()
#ConsumerThread().start()
#当队列中没有任何数据的时候，消费者应该停止运行并等待(wait），而不是继续尝试进行消耗。
# 而当生产者在队列中加入数据之后，应该有一个渠道去告诉（notify）消费者。
# 然后消费者可以再次从队列中进行消耗，而IndexError不再出现。
#条件（condition）可以让一个或多个线程进入wait，直到被其他线程notify。
class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            #产生锁
            condition.acquire()
            num = random.choice(nums)
            queue.append(num)
            print ("Produced",num)
            #如果产生了产品，队列不为空，就发消息
            condition.notify()
            #消息发送后释放锁
            condition.release()
            time.sleep(random.random())
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            #产生锁
            condition.acquire()
            #队列为空
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                #消费者没有东西消费的时候，开始等待
                condition.wait()
                print ("Producer added something to queue and notified the consumer")
            #从队列中取出第一个
            num = queue.pop(0)
            print ("Consumed",num)
            condition.release()
            time.sleep(random.random())
#ProducerThread().start()
#ConsumerThread().start()
#对于消费者，在消费前检查队列是否为空。
#如果为空，调用condition实例的wait()方法。
#消费者进入wait()，同时释放所持有的lock。
#除非被notify，否则它不会运行。
#生产者可以acquire这个lock，因为它已经被消费者release。
#当调用了condition的notify()方法后，消费者被唤醒，但唤醒不意味着它可以开始运行。
#notify()并不释放lock，调用notify()后，lock依然被生产者所持有。
#生产者通过condition.release()显式释放lock。
#消费者再次开始运行，现在它可以得到队列中的数据而不会出现IndexError异常。


#为队列增加大小限制
#生产者不能向一个满队列继续加入数据。
#它可以用以下方式来实现：
#在加入数据前，生产者检查队列是否为满。
#如果不为满，生产者可以继续正常流程。
#如果为满，生产者必须等待，调用condition实例的wait()。
#消费者可以运行。消费者消耗队列，并产生一个空余位置。
#然后消费者notify生产者。
#当消费者释放lock，消费者可以acquire这个lock然后往队列中加入数据。
class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            #条件锁
            condition.acquire()
            if len(queue) == MAX_NUM:
                print ("queue full, producer is waiting")
                condition.wait()
                print ("space in queue, Consumer notified the producer")
            num = random.choice(nums)
            queue.append(num)
            print ("Produce",num)
            condition.notify()
            condition.release()
            time.sleep(random.random())
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print ("Nothing in queue,consumer is waiting")
                condition.wait()
                print ("Producer add something to queue and notified the consumed")
            num = queue.pop(0)
            print ("Consumed",num)
            condition.notify()
            condition.release()
            time.sleep(random.random())
#ProducerThread().start()
#ConsumerThread().start()
#Queue封装了Condition的行为，如wait()，notify()，acquire()。
#Python3中Queue改成了queue
queue1 = queue.Queue(10)
class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue1
        while True:
            num = random.choice(nums)
            queue1.put(num)
            print ("Produced",num)
            time.sleep(random.random())
class ConsumerThread(Thread):
    def run(self):
        global queue1
        while True:
            num = queue1.get()
            queue1.task_done()
            print ("Consumed",num)
            time.sleep(random.random())
ProducerThread().start()
ConsumerThread().start()








