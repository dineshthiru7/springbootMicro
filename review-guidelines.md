# 🔧 React Project MR Review Guidelines

## ✍️ Naming Conventions
- File names: Use **camelCase** (e.g., `userProfile.jsx`)
- Component names: **PascalCase** (e.g., `UserProfile`)
- Variables and functions: **camelCase**
- Constants: **UPPER_SNAKE_CASE**
- Avoid short, ambiguous names (e.g., `a`, `x1`, `temp`)

## 📦 Folder Structure
- Group components logically inside `/components`
- Use `/hooks` for custom hooks, `/services` for API calls

## ❗ Code Practices
- Avoid hardcoded strings/numbers — use constants/configs
- Use `useEffect`/`useMemo` appropriately
- Follow DRY and KISS principles

## 🚫 What to Avoid
- Unused variables/imports
- Console logs or debug code
- Inline styling in components

## ✅ Must Haves
- At least one test per new component/hook
- Clear and relevant PR descriptions with ticket references