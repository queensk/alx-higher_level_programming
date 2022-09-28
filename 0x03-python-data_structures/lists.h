#ifndef LISTS_H
#define LISTS_H

/**
 * structure listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 * 
 * Description: singlylinked list node structure
 */

typedef struct listint_s
{
        int n;
        struct listint_s *next;
} listint_t;

size_t print_listint_(const listint_t *h);
listint *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *get_nodeint_at_index(list_t *head, unsigned int index);
size_t listint_len(const listint_t *h);
int is_palindrome(listint_t **head);

# endif /* LISTS_H */
