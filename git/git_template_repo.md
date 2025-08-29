A **GitHub template repository** is a special type of repo you can mark as a **template**, so others (or you) can use it as a **starting point** for new repositories.

Instead of forking (which keeps a connection to the original), a template repo lets you create a **clean copy** with all the files, structure, and configuration — but without the commit history.

---

## 🔹 What is a Template Repository?

* A **boilerplate repo** you can reuse for similar projects.
* Example: A standard repo with your **CI/CD setup, coding guidelines, linter configs, Docker setup, or project scaffolding**.
* When someone clicks **“Use this template”**, GitHub creates a **new repo** with the same contents, branches, and files.
* It’s especially useful for:

  * Starter code (e.g., React app boilerplate, Selenium test framework)
  * Company-wide coding standards
  * Personal project scaffolds

---

## 🔹 How to Create a Template Repo

1. **Create a normal repository** (or open an existing one).
2. On GitHub, go to the repo **Settings**.
3. Under the **General** section, scroll to **Template Repository**.
4. Check **“Template repository”**. ✅

   * This converts the repo into a template.
5. Now on the repo’s homepage, you (and others) will see a green button **“Use this template” → Create a new repository**.

---

## 🔹 How to Use a Template Repo

* Go to the template repo page.
* Click **Use this template → Create a new repository**.
* Enter the new repo name, description, visibility (public/private).
* Click **Create repository from template**.
* You’ll get a new repo with the same files, but **without commit history**.

---

## 🔹 Advanced Setup (Optional)

You can define extra config for templates:

* **Default branches** (like `main` or `develop`).
* **Labels, issues, workflows** → included automatically.
* **GitHub Actions** pipelines in the `.github/workflows` folder.
* Use `.gitignore` and `LICENSE` files so new repos are preconfigured.

---

✅ In short:
A **template repository** = reusable boilerplate repo → "Use this template" → new repo created without history.
It’s the clean way to standardize and bootstrap projects.

---