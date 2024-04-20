from heap import Heap
from heap import LFUNode


def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0

    # 힙을 생성하여 LFU 노드를 저장합니다.
    lfu_heap = Heap()

    # 캐시를 딕셔너리로 초기화합니다.
    cache = {}
    fre = {}

    data_file = open("linkbench.trc")

    for line in data_file.readlines():
        lpn = line.split()[0]
        
        tot_cnt += 1

        if lpn in cache:
            # LFU 캐시에 LPN이 이미 존재하는 경우
            cache_hit += 1
            fre[lpn].frequency += 1
            lfu_heap.find(fre[lpn])  # LFUNode 객체를 힙에서 찾습니다.
        else:
            if len(cache) >= cache_slots:
                # 캐시가 꽉 찼으면 LFU 교체 알고리즘을 수행합니다.
                lru_node = lfu_heap.deleteMin()  # LFUNode 객체를 힙에서 삭제합니다.
                del cache[lru_node.lpn]

            if lpn in fre:
                # LPN이 빈도수 딕셔너리에 있는 경우
                fre[lpn].frequency += 1
                lfu_heap.insert(fre[lpn])

            else:
                # LPN이 빈도수 딕셔너리에 없는 경우 새로운 노드 생성
                new_node = LFUNode(lpn, 1)
                fre[lpn] = new_node
                lfu_heap.insert(new_node)  # 새로운 LFUNode 객체를 힙에 삽입합니다.

            cache[lpn]=True


    # 파일을 닫고 결과 출력
    data_file.close()
    print("cache_slot =", cache_slots, "cache_hit =", cache_hit, "hit ratio =", cache_hit / tot_cnt)

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        lfu_sim(cache_slots)
