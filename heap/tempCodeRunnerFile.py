if len(cache) < cache_slots:
                cache[lpn] = new_node
                fre[lpn] = new_node
                lfu_heap.insert(new_node)  # LFUNode 객체를 힙에 삽입합니다.
            else:
                # 캐시가 꽉 찼으면 LFU 교체 알고리즘을 수행합니다.
                lru_node = lfu_heap.deleteMin()  # LFUNode 객체를 힙에서 삭제합니다.
                del cache[lru_node.lpn]
                cache[lpn] = new_node

                lfu_heap.insert(new_node)  # 새로운 LFUNode 객체를 힙에 삽입합니다.
