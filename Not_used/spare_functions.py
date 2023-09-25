

def auto_scroll1():
    scroll_speed = 0.001
    count = 0
    item_ids = tree.get_children()  # Get the list of item IDs
    total_items = len(item_ids)
    print(f"Number of items in the tree: {total_items}")
    current_pos = tree.yview()[0]
    tree.yview_moveto(current_pos + scroll_speed)
    new_pos = current_pos + scroll_speed
    print(f"new position: {new_pos}")
    print(f"current position: {current_pos}")
    if current_pos >= 0.77:
        count += 1
        print(f"count: {count}")
        # print(current_pos)
        tree.yview_moveto(0.0)  # Reset to the top if reached the bottom

    window.after(1000, auto_scroll)  # Adjust the update interval here


def auto_scroll1():
    count = 0
    item_ids = tree.get_children()  # Get the list of item IDs
    total_items = len(item_ids)
    print(f"Number of items in the tree: {total_items}")
    while count != total_items:
        current_pos = tree.yview()[0]
        tree.yview_moveto(current_pos + scroll_speed)
        new_pos = current_pos + scroll_speed

        count += 1
        print(f"count: {count}")
        if current_pos >= 0.77:
            #count += 1
            #print(f"count: {count}")
            # print(current_pos)
            tree.yview_moveto(0.0)  # Reset to the top if reached the bottom
        window.after(1000, auto_scroll)  # Adjust the update interval here

def auto_scroll1():
    item_ids = tree.get_children()  # Get the list of item IDs
    total_items = len(item_ids)      # Calculate the number of items


    if total_items == 0:
        return  # No need to scroll if there are no items

    current_pos_tuple = tree.yview()
    current_pos = current_pos_tuple[0]  # Extract the top position from the tuple

    tree.yview_moveto(current_pos + scroll_speed)
    new_pos = current_pos + scroll_speed / total_items
    tree.yview_moveto(new_pos)

    if new_pos >= 1.0:
        new_pos = 0.0  # Reset to the top if reached the bottom

    print(f"The new position is: {new_pos}")
    print(f"Number of items on the tree: {total_items}")
    print(f"Current position: {current_pos}")

    tree.yview_moveto(new_pos)
    window.after(1000, auto_scroll)

def auto_scroll1():
    item_ids = tree.get_children()  # Get the list of item IDs
    total_items = len(item_ids)      # Calculate the number of items
    print(f"Number of item on the tree: {total_items}")

    if total_items == 0:
        return  # No need to scroll if there are no items

    current_pos_tuple = tree.yview()
    current_pos = current_pos_tuple[0]# Extract the top position from the tuple
    print(f" current position: {current_pos}")
    new_pos = current_pos + scroll_speed / total_items
    print(f"The new position is: {new_pos}")

    if new_pos >= 1.0:
        new_pos = 0.0  # Reset to the top if reached the bottom

    tree.yview_moveto(new_pos)
    window.after(1000, auto_scroll)  # Adjust the update interval here


