#include "lists.h"
/**
 *insert_node - Insert a number in a sorted linked list
 *@head: The head or first node of the linked list
 *@number: Number that we want to insert in the linked list
 *Return: Return the adreess of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->next = NULL;
	new_node->n = number;

	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *temp = *head;

		while (temp->next != NULL && temp->next->n < new_node->n)
		{
			temp = temp->next;
		}
		new_node->next = temp->next;
		temp->next = new_node;
	}
	return (new_node);
}
