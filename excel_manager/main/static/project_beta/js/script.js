// js/script.js

// Функция для имитации скачивания таблицы
function downloadTable() {
  alert("Начало загрузки таблицы...");
  // Здесь можно добавить логику скачивания файла, если бы был бэкенд
}

// Функция для печати таблицы
function printTable() {
  window.print();
}

// Пример обработки форм (без реальной отправки данных)
document.addEventListener('DOMContentLoaded', function () {
  // Обработка формы входа
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
      e.preventDefault();
      // Имитация входа в систему
      alert('Вход выполнен успешно!');
      // Перенаправляем пользователя в личный кабинет (например, user_dashboard.html)
      window.location.href = 'user_dashboard.html';
    });
  }
  
  // Обработка формы регистрации
  const registerForm = document.getElementById('register-form');
  if (registerForm) {
    registerForm.addEventListener('submit', function (e) {
      e.preventDefault();
      alert('Регистрация прошла успешно!');
      window.location.href = 'index.html';
    });
  }
  
  // Обработка формы редактирования профиля
  const editProfileForm = document.getElementById('edit-profile-form');
  if (editProfileForm) {
    editProfileForm.addEventListener('submit', function (e) {
      e.preventDefault();
      alert('Данные профиля сохранены!');
      window.location.href = 'user_dashboard.html';
    });
  }
  
  // Обработка формы добавления организации
  const addOrgForm = document.getElementById('add-organization-form');
  if (addOrgForm) {
    addOrgForm.addEventListener('submit', function (e) {
      e.preventDefault();
      alert('Организация добавлена!');
      window.location.href = 'admin_dashboard.html';
    });
  }
});
