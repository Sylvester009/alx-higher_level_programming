#include "lists.h"

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
* reverse_listint - Reverses a singly-linked listint_t list.
* @head: A pointer to the starting node
*
* Returns: A pointer to the head of the reversed list
*/

listint_t *reverse_list(listint_t **head)
{
listint_t *current = *head, *next_node, *prev_node = NULL;

while (current)
{
next_node = current->next;
current->next = prev_node;
prev_node = current;
current = next_node;
}

*head = prev_node;
return (*head);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the linked list.
*
* Returns: 1 if the linked list is a palindrome, 0 otherwise.
*/

int is_palindrome(listint_t **head)
{
listint_t *slow_ptr, *fast_ptr, *tmp_node,
*rev_half, *mid_node;
size_t list_size = 0, i;

/* Check for an empty list or a single-node list (palindrome by definition) */
if (*head == NULL || (*head)->next == NULL)
return (1);

/* Initialize pointers for finding the middle */
slow_ptr = *head;
fast_ptr = *head;

/* Calculate the size of the linked list and find the middle */
tmp_node = *head;
while (tmp_node)
{
list_size++;
tmp_node = tmp_node->next;
}

tmp_node = *head;
for (i = 0; i < (list_size / 2) - 1; i++)
tmp_node = tmp_node->next;

/* Adjust pointers for even-sized lists */
if ((list_size % 2) == 0 && tmp_node->n != tmp_node->next->n)
return (0);

tmp_node = tmp_node->next->next;
rev_half = reverse_list(&tmp_node);
mid_node = rev_half;

tmp_node = *head;

/* Compare the first half with the reversed second half */
while (rev_half)
{
if (tmp_node->n != rev_half->n)
return (0);

tmp_node = tmp_node->next;
rev_half = rev_half->next;
}

/* Reverse the second half back to its original order */
reverse_list(&mid_node);

return 1;
}
