/*
Linked List
*/

#include <stdio.h>
#include <stdlib.h>
struct node {
    int data;
    struct node *next;
};

int main(){
    struct node *node1 = (struct node *) malloc(sizeof(struct node));
    struct node *node2 = (struct node *) malloc(sizeof(struct node));
    struct node *node3 = (struct node *) malloc(sizeof(struct node));
    
    node1->data = 10;
    node1->next = node2;

    node2->data = 20;
    node2->next = node3;

    node3->data = 30;
    node3->next = NULL;

    struct node *current = node1;
    while (current != NULL){
        printf("%d -->",current->data);
        current = current->next;
    }
    printf("NULL\n");

    free(node1);
    free(node2);
    free(node3);

    return 0;

}