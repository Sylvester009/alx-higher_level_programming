#include "lists.h"

/**
* check_cycle - checks if singly linked list has a cycle.
* @list: head of list
* Description - check for loops in list
* Return: 1 (no-cycle) else 0 (cycle)
*/

int check_cycle(listint_t *list)
{
struct listint_t *t;
struct listint_t *h;

t = list;
h = list->next;
  
if (!list)
return (0);

while (h && t && h->next)
{
if (t == h)
{
return (1);
}
h = h->next;
t = t->next->next;
}
return (0);
}
