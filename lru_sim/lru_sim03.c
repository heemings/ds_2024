#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char data[100]; 
    struct Node* next;
} Node;

typedef struct CircularLinkedList {
    Node* head;
    Node* tail;
} CircularLinkedList;

//Circular Linked List 초기화 함수
void initialize(CircularLinkedList* list) {
    list->head = NULL;
    list->tail = NULL;
}

//Circular Linked List 노드 추가 함수
void append(CircularLinkedList* list, const char* data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (new_node == NULL) {
        perror("error");
        exit(EXIT_FAILURE);
    }
    strcpy(new_node->data, data);
    new_node->next=NULL;
    
    if (list->head==NULL) {
        list->head=new_node;
    } else {
        list->tail->next=new_node;
    }
    list->tail=new_node;
    list->tail->next=list->head;
}

//Circular Linked List 노드 삭제 함수
int removeNode(CircularLinkedList* list, const char* data) {
    Node* current=list->head;
    Node* prev=NULL;
    while (current != NULL) {
        if (strcmp(current->data, data) == 0) {
            if (prev != NULL) {
                prev->next = current->next;
                if (current == list->head) {
                    list->head = current->next;
                }
                if (current == list->tail) {
                    list->tail = prev;
                }
            } else {
                list->head = current->next;
                if (current == list->tail) {
                    list->tail = NULL;
                }
            }
            free(current);
            return 1;
        }
        prev = current;
        current = current->next;
        if (current == list->head) {
            break;
        }
    }
    return 0; // 노드를 찾지 못함
}

//Circular Linked List에서 데이터 포함 여부 확인
int contains(CircularLinkedList* list, const char* data) {
    Node* current = list->head;
    while (current != NULL) {
        if (strcmp(current->data, data) == 0) {
            return 1;
        }
        current = current->next;
        if (current == list->head) {
            break;
        }
    }
    return 0; // 데이터를 찾지 못함
}


typedef struct CacheSimulator {
    int cache_slots;
    CircularLinkedList cache;
    int cache_size;
    int cache_hit;
    int tot_cnt;
} CacheSimulator;

//Cache Simulator 초기화 함수
void initializeCacheSimulator(CacheSimulator* cache_sim, int cache_slots) {
    cache_sim->cache_slots = cache_slots;
    initialize(&cache_sim->cache);
    cache_sim->cache_size = 0;
    cache_sim->cache_hit = 0;
    cache_sim->tot_cnt = 0;
}

//Cache Simulator 시뮬레이션 함수
void doSim(CacheSimulator* cache_sim, const char* page) {
    cache_sim->tot_cnt++;
    if (contains(&cache_sim->cache, page)) {
        removeNode(&cache_sim->cache, page);
        append(&cache_sim->cache, page);
        cache_sim->cache_hit++;
    } else {
        if (cache_sim->cache_size >= cache_sim->cache_slots) {
            removeNode(&cache_sim->cache, cache_sim->cache.head->data);

            cache_sim->cache_size--;
        }
        append(&cache_sim->cache, page);
        cache_sim->cache_size++;
    }
}

//결과 출력 함수
void printStats(CacheSimulator* cache_sim) {
    printf("cache_slot = %d, cache_hit = %d, hit ratio = %.5f\n", cache_sim->cache_slots, cache_sim->cache_hit, (float)cache_sim->cache_hit / cache_sim->tot_cnt);
}

int main() {
    FILE* data_file = fopen("./linkbench.trc", "r");
    if (data_file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[100];
    int cache_slots;
    CacheSimulator cache_sim;

    for (cache_slots = 100; cache_slots <= 1000; cache_slots += 100) {
        initializeCacheSimulator(&cache_sim, cache_slots);
        while (fgets(line, sizeof(line), data_file) != NULL) {
            char page[100];
            sscanf(line, "%s", page);
            doSim(&cache_sim, page);
        }
        printStats(&cache_sim);
        rewind(data_file);
    }

    fclose(data_file);
    return 0;
}
