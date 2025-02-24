// API Configuration
const API_URL = 'http://127.0.0.1:5000/api';

// DOM Elements
const computersContainer = document.getElementById('computers-container');
const computerDetailsSection = document.getElementById('computer-details');
const closeDetailsBtn = document.getElementById('close-details');
const detailName = document.getElementById('detail-name');
const gradesList = document.getElementById('grades-list');
const gradeAverageValue = document.getElementById('grade-average-value');
const searchInput = document.getElementById('search-input');

// Modal Elements
const addComputerBtn = document.getElementById('add-computer-btn');
const addComputerModal = document.getElementById('add-computer-modal');
const addComputerForm = document.getElementById('add-computer-form');
const addGradeBtn = document.getElementById('add-grade-btn');
const addGradeModal = document.getElementById('add-grade-modal');
const addGradeForm = document.getElementById('add-grade-form');
const editNameBtn = document.getElementById('edit-name-btn');
const editNameModal = document.getElementById('edit-Name-modal');
const editNameForm = document.getElementById('edit-Name-form');
const updatedNameInput = document.getElementById('updated-Name');

// Close buttons
const modalCloseButtons = document.querySelectorAll('.modal-close, .modal-cancel');

// Current computer
let currentComputerId = null;

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    fetchComputers();
    setupEventListeners();
});

// Setup Event Listeners
function setupEventListeners() {
    // Close details panel
    closeDetailsBtn.addEventListener('click', () => {
        computerDetailsSection.classList.add('hidden');
    });

    // Modal open buttons
    addComputerBtn.addEventListener('click', () => openModal(addComputerModal));
    addGradeBtn.addEventListener('click', () => openModal(addGradeModal));
    editNameBtn.addEventListener('click', () => {
        updatedNameInput.value = detailName.textContent;
        openModal(editNameModal);
    });

    // Modal close buttons
    modalCloseButtons.forEach(button => {
        button.addEventListener('click', event => {
            const modal = event.target.closest('.modal-overlay');
            closeModal(modal);
        });
    });

    // Form submissions
    addComputerForm.addEventListener('submit', handleAddcomputer);
    addGradeForm.addEventListener('submit', handleAddGrade);
    editNameForm.addEventListener('submit', handleUpdateName);

    // Search functionality
    searchInput.addEventListener('input', handleSearch);
}

// API Functions
async function fetchComputers() {
    try {
        const response = await fetch(`${API_URL}/computers`);
        const computers = await response.json();
        renderComputersList(computers);
    } catch (error) {
        showError('שגיאה בטעינת רשימת התלמידים');
        console.error('Error fetching computers:', error);
    }
}

async function fetchComputerDetails(computerData) {
    try {
        const response = await fetch(`${API_URL}/computers/${computerData}`);
        const computer = await response.json();
        
        if (response.ok) {
            renderComputerDetails(computer);
            currentComputerData = computerData;
        } else {
            showError(computer.error || 'שגיאה בטעינת פרטי התלמיד');
        }
    } catch (error) {
        showError('שגיאה בטעינת פרטי התלמיד');
        console.error('Error fetching computer details:', error);
    }
}

async function addComputer(computerData) {
    try {
        const response = await fetch(`${API_URL}/computers`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(computerData)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            return { success: true, data: result };
        } else {
            return { success: false, error: result.error || 'שגיאה בהוספת תלמיד חדש' };
        }
    } catch (error) {
        console.error('Error adding computer:', error);
        return { success: false, error: 'שגיאת תקשורת עם השרת' };
    }
}

async function updateComputerName(detailName, newName) {
    try {
        const response = await fetch(`${API_URL}/computers/${detailName}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: newName })
        });
        
        const result = await response.json();
        
        if (response.ok) {
            return { success: true, data: result };
        } else {
            return { success: false, error: result.error || 'שגיאה בעדכון השם' };
        }
    } catch (error) {
        console.error('Error updating name:', error);
        return { success: false, error: 'שגיאת תקשורת עם השרת' };
    }
}

// Event Handlers
function handleComputerClick(computerData) {
    fetchComputerDetails(computerData);
    computerDetailsSection.classList.remove('hidden');
}

function handleSearch(event) {
    const searchTerm = event.target.value.toLowerCase();
    const computerItems = computersContainer.querySelectorAll('.computer-item');
    
    computerItems.forEach(item => {
        const name = item.querySelector('.computer-name').textContent.toLowerCase();
        const data = item.querySelector('.computer-data').textContent;
        
        if (name.includes(searchTerm) || data.includes(searchTerm)) {
            item.style.display = '';
        } else {
            item.style.display = 'none';
        }
    });
}

async function handleUpdateName(event) {
    event.preventDefault();
    
    const newName = updatedNameInput.value;
    
    if (!currentComputerData) {
        showError('לא נבחר תלמיד');
        return;
    }
    
    const result = await updateComputerName(currentComputerData, newName);
    
    if (result.success) {
        closeModal(editNameModal);
        showSuccess('השם עודכנה בהצלחה');
        renderComputerDetails(result.data);
    } else {
        showError(result.error);
    }
}

// UI Rendering Functions
function renderComputersList(computers) {
    computersContainer.innerHTML = '';
    
    if (computers.length === 0) {
        computersContainer.innerHTML = '<p class="empty-state">לא נמצאו מחשבים</p>';
        return;
    }
    
    computers.forEach(computer => {
        const computerElement = document.createElement('li');
        computerElement.className = 'computer-item';
        const maxLength = 30;
        computerElement.innerHTML = `
            <div>
                <span class="computer-name">${computer.name.length > maxLength ? computer.name.slice(0, maxLength) + "..." : computer.name}</span>
            </div>
            <span class="computer-data">${computer.data.length > maxLength ? computer.data.slice(0, maxLength) + "..." : computer.data}</span>
        `;
        
        computerElement.addEventListener('click', () => handleComputerClick(computer.data));
        computersContainer.appendChild(computerElement);
    });
}

function renderComputerDetails(computer) {
    detailName.textContent = computer.name;
    
    // Render grades
    gradesList.innerHTML = '';
}

// Helper Functions
function openModal(modal) {
    modal.classList.remove('hidden');
    // Prevent body scrolling when modal is open
    document.body.style.overflow = 'hidden';
}

function closeModal(modal) {
    modal.classList.add('hidden');
    // Restore body scrolling
    document.body.style.overflow = '';
}

// Notifications
function showSuccess(message) {
    showNotification(message, 'success');
}

function showError(message) {
    showNotification(message, 'error');
}

function showNotification(message, type) {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => {
        notification.remove();
    });
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    // Add icon based on type
    const icon = document.createElement('i');
    icon.className = type === 'success' ? 'fas fa-check-circle' : 'fas fa-exclamation-circle';
    notification.prepend(icon);
    
    // Add close button
    const closeBtn = document.createElement('button');
    closeBtn.className = 'notification-close';
    closeBtn.innerHTML = '<i class="fas fa-times"></i>';
    closeBtn.addEventListener('click', () => {
        notification.remove();
    });
    notification.appendChild(closeBtn);
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Style the notification
    Object.assign(notification.style, {
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        padding: '1rem 1.5rem',
        borderRadius: '8px',
        display: 'flex',
        alignItems: 'center',
        gap: '0.75rem',
        zIndex: '2000',
        boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
        animation: 'slideIn 0.3s forwards'
    });
    
    if (type === 'success') {
        notification.style.backgroundColor = '#f6ffed';
        notification.style.color = '#52c41a';
        notification.style.border = '1px solid #b7eb8f';
    } else {
        notification.style.backgroundColor = '#fff1f0';
        notification.style.color = '#f5222d';
        notification.style.border = '1px solid #ffa39e';
    }
    
    // Add CSS animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    `;
    document.head.appendChild(style);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s forwards';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 5000);
    
    // Add slideOut animation
    style.textContent += `
        @keyframes slideOut {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
    `;
}