Sure, I'll provide you with a basic structure for a React.js application using TypeScript that allows for CRUD operations on customer data. This example will include:

1. **Setting up the project with Create React App**
2. **Creating a basic customer interface**
3. **Creating components for listing, adding, editing, and deleting customers**
4. **Managing state with React hooks**

### Step 1: Set Up the Project

1. **Create a new React project with TypeScript:**
   ```bash
   npx create-react-app customer-crud --template typescript
   cd customer-crud
   ```

2. **Install additional dependencies (optional):**
   ```bash
   npm install axios
   ```

### Step 2: Define Customer Interface

Create a `types.ts` file to define the customer interface:
```typescript
// src/types.ts
export interface Customer {
  id: number;
  name: string;
  email: string;
  phone: string;
}
```

### Step 3: Create Components

#### 1. CustomerList Component

```typescript
// src/components/CustomerList.tsx
import React from 'react';
import { Customer } from '../types';

interface CustomerListProps {
  customers: Customer[];
  onEdit: (customer: Customer) => void;
  onDelete: (customerId: number) => void;
}

const CustomerList: React.FC<CustomerListProps> = ({ customers, onEdit, onDelete }) => {
  return (
    <div>
      <h2>Customer List</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {customers.map(customer => (
            <tr key={customer.id}>
              <td>{customer.name}</td>
              <td>{customer.email}</td>
              <td>{customer.phone}</td>
              <td>
                <button onClick={() => onEdit(customer)}>Edit</button>
                <button onClick={() => onDelete(customer.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomerList;
```

#### 2. CustomerForm Component

```typescript
// src/components/CustomerForm.tsx
import React, { useState, useEffect } from 'react';
import { Customer } from '../types';

interface CustomerFormProps {
  customer: Customer | null;
  onSave: (customer: Customer) => void;
}

const CustomerForm: React.FC<CustomerFormProps> = ({ customer, onSave }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');

  useEffect(() => {
    if (customer) {
      setName(customer.name);
      setEmail(customer.email);
      setPhone(customer.phone);
    }
  }, [customer]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const newCustomer: Customer = {
      id: customer ? customer.id : Date.now(),
      name,
      email,
      phone,
    };
    onSave(newCustomer);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{customer ? 'Edit Customer' : 'Add Customer'}</h2>
      <div>
        <label>Name:</label>
        <input type="text" value={name} onChange={e => setName(e.target.value)} />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
      </div>
      <div>
        <label>Phone:</label>
        <input type="text" value={phone} onChange={e => setPhone(e.target.value)} />
      </div>
      <button type="submit">{customer ? 'Update' : 'Add'}</button>
    </form>
  );
};

export default CustomerForm;
```

### Step 4: Manage State and CRUD Operations in App Component

```typescript
// src/App.tsx
import React, { useState } from 'react';
import { Customer } from './types';
import CustomerList from './components/CustomerList';
import CustomerForm from './components/CustomerForm';

const App: React.FC = () => {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [selectedCustomer, setSelectedCustomer] = useState<Customer | null>(null);

  const handleSaveCustomer = (customer: Customer) => {
    if (selectedCustomer) {
      setCustomers(customers.map(c => (c.id === customer.id ? customer : c)));
    } else {
      setCustomers([...customers, customer]);
    }
    setSelectedCustomer(null);
  };

  const handleEditCustomer = (customer: Customer) => {
    setSelectedCustomer(customer);
  };

  const handleDeleteCustomer = (customerId: number) => {
    setCustomers(customers.filter(c => c.id !== customerId));
  };

  return (
    <div className="App">
      <h1>Customer CRUD Application</h1>
      <CustomerForm customer={selectedCustomer} onSave={handleSaveCustomer} />
      <CustomerList
        customers={customers}
        onEdit={handleEditCustomer}
        onDelete={handleDeleteCustomer}
      />
    </div>
  );
};

export default App;
```

### Step 5: Basic Styling (Optional)

Add some basic styling for better presentation.

```css
/* src/App.css */
.App {
  font-family: Arial, sans-serif;
  padding: 20px;
}

h1, h2 {
  color: #333;
}

form {
  margin-bottom: 20px;
}

form div {
  margin-bottom: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

table, th, td {
  border: 1px solid #ddd;
}

th, td {
  padding: 8px;
  text-align: left;
}

button {
  margin-right: 5px;
}
```

### Conclusion

This example provides a basic setup for a React.js application using TypeScript to perform CRUD operations on customer data. The application includes components for listing customers, adding new customers, editing existing customers, and deleting customers. You can expand this application by adding features like form validation, backend integration, and more sophisticated state management (e.g., using Redux or Context API).
