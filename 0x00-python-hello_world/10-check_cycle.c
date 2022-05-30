#include "lists.h"
/**
 *check_cycle - checks whether a singly linked list has a cycle in it
 *@list:linked list to test
 *Return:0 - no cycle, 1 - cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *rabbit = list, *turtle = list;

	while (rabbit && turtle && rabbit->next)
	{
		rabbit = rabbit->next->next;
		turtle = turtle->next;
		if (rabbit == turtle)
			return (1);
	}
	return (0);
}
