
import multiprocessing

def put_data(queue):
    for i in range(10):
        queue.put(i+1)
        if queue.full():
            break


def get_data(queue):
    for i in range(10):
        print("queue中的数据有: ", queue.get())
        # 取出完毕，跳出
        if queue.empty():
            break


if __name__ == '__main__':
    q = multiprocessing.Queue(3)

    p1 = multiprocessing.Process(target=put_data, args=(q, ))
    p2 = multiprocessing.Process(target=get_data, args=(q, ))

    # 放完数据以后在获取
    p1.start()
    p1.join()

    # p2在进行获取
    p2.start()
