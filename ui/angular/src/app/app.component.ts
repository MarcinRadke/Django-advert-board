import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular';

  number:number=0;
  showAbout(){
    if (this.number == 1){
      this.number=0
      return "App made in Angular for showing, filtering Django database"
    }
    this.number=1
    return ""
  }
}
