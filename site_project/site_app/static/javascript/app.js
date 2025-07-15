let tabIdPanier=[]

function ouverture(){
    let bouton = document.querySelector(".home_plus");
    bouton.style.display = 'block'
}



let compteur = document.querySelector(".base_panier");
if(localStorage.getItem('panier') == null){
    var panier = {};
}
else{
    panier = JSON.parse(localStorage.getItem('panier'));
}
compteur.innerHTML = Object.keys(panier).length;

function compteur_panier(element){
    console.log('ajouter');
    item_id = element.id.toString();
    console.log(item_id);
    if(panier[item_id]!=undefined){
        //Creons une a l'interieur du dictio
        quantite = panier[item_id][0] +1
        panier[item_id][0] = quantite;
       // panier[item_id] = panier[item_id] +1;
    }
    else{
        quantite = 1;
        nom = document.getElementById("art"+item_id).innerHTML;
        panier[item_id] = [quantite, nom];
        
       // panier[item_id] = 1;
    }
    console.log(panier);
    localStorage.setItem('panier', JSON.stringify(panier));

    //avoir la longeur de notre dictionaire panier dans le localstorage
    // elle doit se calculer en fonction des cles
    console.log(Object.keys(panier).length);
    
    compteur.innerHTML = Object.keys(panier).length;
}

function AfficherListePanier(panier){
  
}


