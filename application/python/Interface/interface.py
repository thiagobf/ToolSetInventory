import sqlite3
import streamlit as st

DB_NAME = "items.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, name, quantity FROM items ORDER BY id")
    rows = c.fetchall()
    conn.close()
    return rows

def add_item(name, quantity):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()

def update_item(item_id, name, quantity):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE items SET name = ?, quantity = ? WHERE id = ?", (name, quantity, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

init_db()

st.title("Simple CRUD with Streamlit")

with st.form("add_form"):
    name = st.text_input("Name")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    submitted = st.form_submit_button("Add Item")
    if submitted:
        if name:
            add_item(name, int(quantity))
            st.success("Item added!")
            st.rerun()

st.subheader("Items")

items = get_items()

if items:
    for item_id, name, quantity in items:
        col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
        col1.write(name)
        col2.write(quantity)

        with st.form(f"edit_{item_id}"):
            new_name = st.text_input("Edit name", value=name, key=f"name_{item_id}")
            new_quantity = st.number_input("Edit quantity", min_value=0, step=1, value=int(quantity), key=f"qty_{item_id}")
            submitted = st.form_submit_button("Update", key=f"update_{item_id}")
            if submitted:
                update_item(item_id, new_name, int(new_quantity))
                st.success("Item updated!")
                st.rerun()

        if st.button("Delete", key=f"delete_{item_id}"):
            delete_item(item_id)
            st.success("Item deleted!")
            st.rerun()
else:
    st.info("No items yet.")