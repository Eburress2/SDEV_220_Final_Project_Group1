// document.addEventListener('DOMContentLoaded', function () {
//     const addItemButton = document.querySelector('#add-item');
//     const orderItemsContainer = document.querySelector('#order-items');
//     const subtotalInput = document.querySelector('#subtotal');

//     // Get product data from the hidden div
//     const productData = JSON.parse(document.querySelector('#product-data').dataset.products);

//     function updateSubtotal() {
//         let subtotal = 0;
//         document.querySelectorAll('.item-row').forEach(row => {
//             const price = parseFloat(row.querySelector('.item-price').value);
//             const quantity = parseInt(row.querySelector('.item-quantity').value);
//             subtotal += price * quantity;
//         });
//         subtotalInput.value = subtotal.toFixed(2);
//     }

//     addItemButton.addEventListener('click', function () {
//         const newItemRow = document.createElement('div');
//         newItemRow.classList.add('item-row', 'mb-3');
//         newItemRow.innerHTML = `
//             <select class="form-select item-product" required>
//                 <option value="">Select Product</option>
//                 ${productData.map(product => `
//                     <option value="${product.id}" data-price="${product.price}">
//                         ${product.name} ($${product.price})
//                     </option>
//                 `).join('')}
//             </select>
//             <input type="number" class="form-control item-quantity" min="1" value="1" required>
//             <button type="button" class="btn btn-danger btn-sm remove-item">Remove</button>
//         `;
//         orderItemsContainer.appendChild(newItemRow);

//         // Add event listeners for the new item
//         newItemRow.querySelector('.item-product').addEventListener('change', updateSubtotal);
//         newItemRow.querySelector('.item-quantity').addEventListener('input', updateSubtotal);
//         newItemRow.querySelector('.remove-item').addEventListener('click', function () {
//             newItemRow.remove();
//             updateSubtotal();
//         });
//     });

//     // Initial subtotal calculation
//     updateSubtotal();
// });