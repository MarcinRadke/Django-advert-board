import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-show-off',
  templateUrl: './show-off.component.html',
  styleUrls: ['./show-off.component.css']
})
export class ShowOffComponent implements OnInit {
  closeResult = '';
  constructor(private service:SharedService, private modalService: NgbModal) { }

  OfferList:any=[];
  CategoryList:any=[];
  OfferIdFilter:string="";
  OfferTitleFilter:string="";
  OfferCategoryFilter:string="";
  OfferListWithoutFilter:any=[];

  ngOnInit(): void {
    this.refreshOffList();
  }

  refreshOffList(){
    this.service.getOfferList().subscribe(data=>{
      this.OfferList=data;
      this.OfferListWithoutFilter=data;
    })
    this.service.getAllCategoryNames().subscribe(data=>{
      this.CategoryList=data;
    })
  }

  getCategoryId(id:string): string{
    if (this.CategoryList != null) {
      return this.CategoryList.find((category:any)=> category.id == id).name;
    }
    return "<Not found>"
  }

  showDetails(id:string): string{
    if (this.OfferList != null) {
      return this.OfferList.find((offer:any)=> offer.id == id).description;
    }
    return "<Not found>"
  }
  showDate(id:string): string{
    if (this.OfferList != null) {
      return this.OfferList.find((offer:any)=> offer.id == id).created_at;
    }
    return "<Not found>"
  }

  open(content:any) {
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'});
  }

  Filtering(){
    var OfferIdFilter = this.OfferIdFilter;
    var OfferTitleFilter = this.OfferTitleFilter;
    var OfferCategoryFilter = this.OfferCategoryFilter;

    this.OfferList = this.OfferListWithoutFilter.filter(function (el:any){
      return el.id.toString().toLowerCase().includes(
        OfferIdFilter.toString().trim().toLowerCase()
      )&&
      el.title.toString().toLowerCase().includes(
        OfferTitleFilter.toString().trim().toLowerCase()
      )&&
      el.category.toString().toLowerCase().includes(
        OfferCategoryFilter.toString().trim().toLowerCase()
      )
    })
  }

}
