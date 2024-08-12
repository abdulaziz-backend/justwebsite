function openModal() {
    document.getElementById('modal').style.display = 'block';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function() {
    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = 'none';
    }
});




document.addEventListener("DOMContentLoaded", function() {
    const friends = [
        { name: "Alice", avatar: "A", blaze: "5000 $BLAZE" },
        { name: "Bob", avatar: "B", blaze: "3000 $BLAZE" },
        { name: "Charlie", avatar: "C", blaze: "1500 $BLAZE" },
        { name: "David", avatar: "D", blaze: "2000 $BLAZE" }
    ];

    const friendsListContainer = document.getElementById('friends-list-container');
    const friendsList = document.getElementById('friends-list');

    if (friends.length > 0) {
        friends.forEach(friend => {
            const friendItem = document.createElement('div');
            friendItem.classList.add('friend-item');

            const avatar = document.createElement('div');
            avatar.classList.add('friend-avatar');
            avatar.textContent = friend.avatar;

            const details = document.createElement('div');
            details.classList.add('friend-details');

            const name = document.createElement('div');
            name.classList.add('friend-name');
            name.textContent = friend.name;

            const blaze = document.createElement('div');
            blaze.classList.add('friend-blaze');
            blaze.textContent = friend.blaze;

            details.appendChild(name);
            details.appendChild(blaze);

            friendItem.appendChild(avatar);
            friendItem.appendChild(details);
            friendsList.appendChild(friendItem);
        });

        friendsListContainer.style.display = 'block';
        
        // Set overflow-y to auto to handle the scrollbar
        if (friends.length > 2) {
            friendsList.style.overflowY = 'auto';
        } else {
            friendsList.style.overflowY = 'hidden';
        }
    }

    const loadingElement = document.getElementById('loading');
    if (loadingElement) {
        loadingElement.style.display = 'none';
    }
});

