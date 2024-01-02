#include "lists.h"

/**
* check_cycle - checks if singly linked list has a cycle.
* @list: head of list
* Description - check for loops in list
* Return: 1 (no-cycle) else 0 (cycle)
*/

int check_cycle(listint_t *list)
{
	listint_t *c;
	listint_t *f;

	if (!list)
		return (0);

	c = list;
	f = list->next;
	while (f && c && f->next)
	{
		c = c->next;
		f = f->next->next;
		
		if (c == f)
		{
			return (1);
		}
	}
	return (0);
}
