## JavaScript interview questions along with explanations in Bangla

**1. JavaScript কি ধরনের ভাষা?**

- উত্তর: JavaScript একটি scripting ভাষা, যা মূলত client-side ওয়েব ডেভেলপমেন্টের জন্য ব্যবহৃত হয়। এটি interpreted language যার মানে এটি সরাসরি browser এ run হয়, কোনো compilation ছাড়াই।

**2. Variable declaration এর ক্ষেত্রে var, let, এবং const এর মধ্যে পার্থক্য কি?**

- উত্তর:
  - `var:` এটি function-scoped, মানে এটি শুধুমাত্র একটি ফাংশনের ভিতরে সীমাবদ্ধ।
  - `let:` এটি block-scoped, মানে এটি শুধুমাত্র `{}` ব্লকের ভিতরে সীমাবদ্ধ থাকে।
  - `const:` এটি block-scoped, কিন্তু এর মান একবার সেট করার পর আর পরিবর্তন করা যায় না।

**3. Closures কী এবং কীভাবে কাজ করে?**

- উত্তর: Closure হলো একটি ফাংশন যা তার বাহিরের scope এর ভ্যারিয়েবলগুলোকে মনে রাখে। Closure এর কারণে inner function তার parent function এর variable access করতে পারে।

**উদাহরণ:**

```js
function outerFunction() {
  let outerVar = "Hello";
  function innerFunction() {
    console.log(outerVar);
  }
  return innerFunction;
}

const closure = outerFunction();
closure(); // Output: Hello
```
