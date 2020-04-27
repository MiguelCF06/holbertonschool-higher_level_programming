#include "lists.h"
/**
 *check_cycle - Check if there is a cycle in the linked list
 *@list: Linked list
 *Return: Return 1 if there is a cycle or 0 is there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
