"""冒泡排序实现。"""


def bubble_sort(values: list[int]) -> list[int]:
    """使用冒泡排序算法，返回 values 的一份排序后的副本。

    算法思路：
      每一轮把当前未排序区间中的最大元素"冒"到区间末尾；
      重复若干轮，直到整个列表有序。
    """
    # 复制一份列表，避免修改调用方传入的原始数据
    result = values.copy()

    # 外层循环控制每一轮的比较区间 [0, end]
    # 每轮结束后，最大值会被放到下标 end 处，因此 end 逐渐减小
    for end in range(len(result) - 1, 0, -1):
        # 标记本轮是否发生过交换
        swapped = False

        # 内层循环从头开始，两两比较相邻元素
        for index in range(end):
            # 如果前一个元素比后一个元素大，则交换它们
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True

        # 如果整轮都没有发生交换，说明列表已经有序，可以提前结束
        if not swapped:
            break

    return result


if __name__ == "__main__":
    # 示例：对一组无序数字进行排序并打印结果
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(numbers))
