import { useEffect, useState } from "react";
import API from "../api/api";

export default function Cart() {
  const [cart, setCart] = useState({ items: [], total: 0 });

  const fetchCart = async () => {
    const res = await API.get("http://localhost:8002/cart/");
    setCart(res.data);
  };

  const removeItem = async (id) => {
    await API.delete(`http://localhost:8002/cart/remove/${id}`);
    fetchCart();
  };

  const checkout = async () => {
    await API.post("http://localhost:8003/orders/checkout");
    alert("Order placed!");
    fetchCart();
  };

  useEffect(() => { fetchCart(); }, []);

  return (
    <div>
      <h2>Cart</h2>
      {cart.items.map(i => (
        <div key={i._id}>
          {i.product_id} - {i.quantity} x {i.price} = {i.total}
          <button onClick={() => removeItem(i._id)}>Remove</button>
        </div>
      ))}
      <h3>Total: {cart.total}</h3>
      <button onClick={checkout}>Checkout</button>
    </div>
  );
}
