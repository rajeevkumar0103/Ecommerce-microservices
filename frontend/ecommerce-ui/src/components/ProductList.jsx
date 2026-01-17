import { useEffect, useState } from "react";
import API from "../api/api";

export default function ProductList({ onAddToCart }) {
  const [products, setProducts] = useState([]);
  const [page, setPage] = useState(1);

  const fetchProducts = async () => {
    const res = await API.get(`http://localhost:8001/products?page=${page}&limit=5`);
    setProducts(res.data.data);
  };

  useEffect(() => { fetchProducts(); }, [page]);

  return (
    <div>
      {products.map(p => (
        <div key={p.id}>
          <h3>{p.name}</h3>
          <p>{p.description}</p>
          <p>Price: {p.price}</p>
          <p>Stock: {p.stock}</p>
          <button onClick={() => onAddToCart(p.id)}>Add to Cart</button>
        </div>
      ))}
      <button onClick={() => setPage(page-1)} disabled={page===1}>Prev</button>
      <button onClick={() => setPage(page+1)}>Next</button>
    </div>
  );
}
