import ProductList from "../components/ProductList";
import API from "../api/api";

export default function Home() {
  const addToCart = async (productId) => {
    await API.post("http://localhost:8002/cart/add", { product_id: productId, quantity: 1 });
    alert("Added to cart");
  };

  return (
    <div>
      <h1>Products</h1>
      <ProductList onAddToCart={addToCart} />
    </div>
  );
}
