async function createPost() {
    const content = document.getElementById('post-content').value;
    const response = await fetch('/api/create-post/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken') // Django requires CSRF token
        },
        body: `content=${encodeURIComponent(content)}`
    });
    if (response.ok) {
        loadFeed(); // Refresh feed
    }
}

async function likePost(postId) {
    await fetch(`/api/like/${postId}/`);
    loadFeed();
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Load Feed (Simplified)
function loadFeed() {
    // Fetch posts from your API and render them here
    console.log("Loading feed...");
}